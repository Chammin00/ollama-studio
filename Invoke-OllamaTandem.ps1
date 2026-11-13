<#
.SYNOPSIS
    Invokes the Antigravity & Ollama Tandem Bridge to coordinate dual-workspace execution.
.DESCRIPTION
    Sends tasks, code files, or initialization protocols to local Ollama models (default: antigravity-skills:latest)
    and streams structured PSCustomObject results for pipeline consumption.
.PARAMETER Task
    The prompt or directive to execute with Ollama in tandem.
.PARAMETER FilePath
    Optional path to a source file or artifact to include as context.
.PARAMETER Model
    The Ollama model tag to invoke (default: 'antigravity-skills:latest').
.PARAMETER InitializeProtocol
    Switch to send OLLAMA_TANDEM_PROTOCOL.txt and activate tandem state.
.EXAMPLE
    Invoke-OllamaTandem -InitializeProtocol
.EXAMPLE
    Invoke-OllamaTandem -Task "Audit baseline compliance" -FilePath ".\app.js"
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Position = 0, ValueFromPipeline = $true, ValueFromPipelineByPropertyName = $true)]
    [string]$Task,

    [Parameter(Position = 1)]
    [string]$FilePath,

    [Parameter()]
    [string]$Model = "antigravity-skills:latest",

    [Parameter()]
    [switch]$InitializeProtocol
)

begin {
    $ErrorActionPreference = 'Stop'
    $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    if (-not $ScriptDir) { $ScriptDir = $PSScriptRoot }
    Set-Location -Path $ScriptDir

    $PythonExe = (Get-Command python -ErrorAction SilentlyContinue).Source
    if (-not $PythonExe) {
        throw [System.IO.FileNotFoundException]"Python runtime was not found in PATH."
    }

    $BridgeScript = Join-Path -Path $ScriptDir -ChildPath "tandem_bridge.py"
    if (-not (Test-Path -Path $BridgeScript)) {
        throw [System.IO.FileNotFoundException]"tandem_bridge.py not found at $BridgeScript"
    }
}

process {
    $ArgList = @("`"$BridgeScript`"", "--model", "`"$Model`"")

    if ($InitializeProtocol) {
        $ArgList += "--init"
    }

    if ($Task) {
        $ArgList += @("--task", "`"$Task`"")
    }

    if ($FilePath) {
        if (-not (Test-Path -Path $FilePath)) {
            Write-Warning "Target context file not found: $FilePath"
        } else {
            $ResolvedPath = (Resolve-Path -Path $FilePath).Path
            $ArgList += @("--file", "`"$ResolvedPath`"")
        }
    }

    if ($PSCmdlet.ShouldProcess("Ollama ($Model)", "Dispatch tandem execution")) {
        $ProcStartInfo = New-Object System.Diagnostics.ProcessStartInfo
        $ProcStartInfo.FileName = $PythonExe
        $ProcStartInfo.Arguments = ($ArgList -join ' ')
        $ProcStartInfo.RedirectStandardOutput = $true
        $ProcStartInfo.RedirectStandardError = $true
        $ProcStartInfo.UseShellExecute = $false
        $ProcStartInfo.CreateNoWindow = $true

        $Process = [System.Diagnostics.Process]::Start($ProcStartInfo)
        $StdOut = $Process.StandardOutput.ReadToEnd()
        $StdErr = $Process.StandardError.ReadToEnd()
        $Process.WaitForExit()

        [PSCustomObject]@{
            ExitCode    = $Process.ExitCode
            Success     = ($Process.ExitCode -eq 0)
            Model       = $Model
            Output      = $StdOut.Trim()
            ErrorOutput = $StdErr.Trim()
            Timestamp   = (Get-Date).ToString("o")
        }
    }
}

end {
}

# Install the figma-app-design-builder skill for Claude Code (Windows PowerShell).
#
# One line, straight from GitHub:
#   irm https://raw.githubusercontent.com/ws0325/AutoFigma-AppDesign/main/install.ps1 | iex
# Or from a cloned copy of this repository:
#   powershell -ExecutionPolicy Bypass -File install.ps1
#
# Options (environment variables):
#   $env:SKILL_SCOPE = "project"   install into .\.claude\skills of the current folder instead of %USERPROFILE%\.claude\skills
#   $env:REPO = "owner/name"       GitHub repository to download from when run outside the repository

$ErrorActionPreference = "Stop"
$Skill  = "figma-app-design-builder"
$Repo   = if ($env:REPO) { $env:REPO } else { "ws0325/AutoFigma-AppDesign" }
$Branch = if ($env:BRANCH) { $env:BRANCH } else { "main" }

if ($env:SKILL_SCOPE -eq "project") {
    $DestRoot = Join-Path (Get-Location) ".claude\skills"
} else {
    $DestRoot = Join-Path $env:USERPROFILE ".claude\skills"
}
$Dest = Join-Path $DestRoot $Skill

# 1. Find the skill folder: next to this script, or download the repository.
$Tmp = $null
$ScriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { $null }
if ($ScriptDir -and (Test-Path (Join-Path $ScriptDir "skills\$Skill"))) {
    $Src = Join-Path $ScriptDir "skills\$Skill"
} else {
    $Tmp =Join-Path ([System.IO.Path]::GetTempPath()) ("skill-" + [guid]::NewGuid())
    New-Item -ItemType Directory -Path $Tmp | Out-Null
    $Zip = Join-Path $Tmp "repo.zip"
    Write-Host "Downloading $Repo@$Branch..."
    Invoke-WebRequest -UseBasicParsing "https://github.com/$Repo/archive/refs/heads/$Branch.zip" -OutFile $Zip
    Expand-Archive -Path $Zip -DestinationPath $Tmp
    $Found = Get-ChildItem -Path $Tmp -Directory -Recurse -Depth 2 | Where-Object { $_.Name -eq $Skill -and $_.Parent.Name -eq "skills" } | Select-Object -First 1
    if (-not $Found) { Write-Host "Skill folder not found in the download." -ForegroundColor Red; exit 1 }
    $Src = $Found.FullName
}

# 2. Copy (replacing an older version).
New-Item -ItemType Directory -Force -Path $DestRoot | Out-Null
if (Test-Path $Dest) { Remove-Item -Recurse -Force $Dest }
Copy-Item -Recurse -Path $Src -Destination $Dest
Get-ChildItem -Path $Dest -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
if ($Tmp) { Remove-Item -Recurse -Force $Tmp }
Write-Host "Installed to $Dest"

# 3. Python image library used by the grid script.
$Py = $null
foreach ($c in @("python", "py")) { if (Get-Command $c -ErrorAction SilentlyContinue) { $Py = $c; break } }
if ($Py) {
    & $Py -c "import PIL" 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Pillow already installed."
    } else {
        Write-Host "Installing Pillow (for scripts\grid_extract.py)..."
        & $Py -m pip install --user --quiet pillow
        if ($LASTEXITCODE -ne 0) { Write-Host "Could not install Pillow automatically. Run: $Py -m pip install pillow" -ForegroundColor Yellow }
    }
} else {
    Write-Host "Python not found. Install it from https://www.python.org/ and then run: python -m pip install pillow" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Done. Restart Claude Code, then try:  design me a fitness app" -ForegroundColor Green

<#
PowerShell helper to create the prepared GitHub issues using `gh` (GitHub CLI).

Prereqs:
- `gh` installed and authenticated (`gh auth login`).
- Run from the repository root.

This script will create issues for the markdown files under `.github/issues/`.
Run it interactively so you can confirm each issue before creation.
#>

param(
    [switch]$AutoConfirm
)

$repoRoot = Split-Path -Parent $PSScriptRoot
$issueDir = Join-Path $repoRoot '.github\issues'
Get-ChildItem -Path $issueDir -Filter "*.md" | ForEach-Object {
    $file = $_.FullName
    $titleLine = Select-String -Path $file -Pattern '^Title:' | Select-Object -First 1
    if ($titleLine) {
        $title = $titleLine -replace '^Title:\s*',''
    } else {
        $title = $_.BaseName
    }
    Write-Host "Preparing to create issue: $title"
    Write-Host "Body file: $file"
    if ($AutoConfirm) {
        $confirm = 'y'
    } else {
        $confirm = Read-Host "Create this issue? (y/N)"
    }
    if ($confirm -ieq 'y') {
        Write-Host "Creating issue: $title"
        $res = gh issue create --title "$title" --body-file "$file" --label "html-validate" 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Created issue: $title"
        } else {
            Write-Host "Failed to create issue: $title"
            Write-Host $res
        }
    } else {
        Write-Host "Skipping $title"
    }
}

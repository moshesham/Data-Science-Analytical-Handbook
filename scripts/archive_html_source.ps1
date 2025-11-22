<#
Archiving helper: moves contents of html_source (except Archive) into html_source/Archive
and commits the changes using git. Run from repository root in PowerShell:
  & .\scripts\archive_html_source.ps1

This script attempts to use 'git mv' for history-preserving moves. If git mv fails for an item
it falls back to a filesystem move then stages the result.
#>

Write-Host "Starting html_source archive process..."

if (-not (Test-Path "html_source")) {
    Write-Host "html_source directory not found; nothing to archive."; exit 0
}

if (-not (Test-Path "html_source/Archive")) {
    New-Item -ItemType Directory -Path "html_source/Archive" -Force | Out-Null
}

$items = Get-ChildItem -Path "html_source" -Force | Where-Object { $_.Name -ne 'Archive' }
foreach ($it in $items) {
    $src = Join-Path -Path "html_source" -ChildPath $it.Name
    $dest = Join-Path -Path "html_source/Archive" -ChildPath $it.Name
    Write-Host "Archiving: $src -> $dest"
    try {
        git mv --force "${src}" "${dest}"
        if ($LASTEXITCODE -ne 0) {
            throw "git mv failed"
        }
    } catch {
        Write-Host ("git mv failed for {0} - attempting filesystem move" -f $src)
        try {
            Move-Item -Path $src -Destination $dest -Force -ErrorAction Stop
            git add "${dest}"
            git rm -f "${src}" -r
            if ($LASTEXITCODE -ne 0) { Write-Host "git rm fallback failed; ensure repo is clean" }
        } catch {
            Write-Host ("Failed to move {0}: {1}" -f $src, $_)
        }
    }
}

Write-Host "Staging and committing archive changes..."
git add -A
if ((git status --porcelain) -ne '') {
    git commit -m "archive: move original html_source content into html_source/Archive/"
    Write-Host "Archive committed."
} else {
    Write-Host "No changes to commit."
}

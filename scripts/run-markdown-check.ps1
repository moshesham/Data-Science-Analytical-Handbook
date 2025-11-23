Param(
  [string]$ConfigPath = ".markdown-link-check.json"
)

$files = @(
  "Best-Practices\Deep_Dive\1_Strategy+Architecture.md",
  "Extra-Review-Problems\sql-example-problems.md",
  "index.md"
)

# Add all _pages markdown files
$pages = Get-ChildItem -Recurse -Path _pages -Filter *.md | Select-Object -ExpandProperty FullName
$files = $files + $pages

$failed = @()
foreach ($f in $files) {
  Write-Host "Checking $f"
  npx -y markdown-link-check -q -c $ConfigPath "$f"
  if ($LASTEXITCODE -ne 0) {
    Write-Host "FAILED: $f" -ForegroundColor Red
    $failed += $f
  } else {
    Write-Host "OK: $f" -ForegroundColor Green
  }
}

if ($failed.Count -gt 0) {
  Write-Host "Summary: " -NoNewline
  Write-Host "$($failed.Count) file(s) failed link check" -ForegroundColor Red
  $failed | ForEach-Object { Write-Host " - $_" }
  exit 1
} else {
  Write-Host "Summary: All checks passed" -ForegroundColor Green
}

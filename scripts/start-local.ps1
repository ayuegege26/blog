$ProjectRoot = Split-Path -Parent $PSScriptRoot
$OutLog = Join-Path $ProjectRoot ".astro-preview.log"
$ErrLog = Join-Path $ProjectRoot ".astro-preview.err.log"
$Node = "C:\Program Files\nodejs\node.exe"
$LocalServer = Join-Path $ProjectRoot "scripts\local-server.mjs"

$existingServer = Get-NetTCPConnection -LocalAddress "127.0.0.1" -LocalPort 4321 -State Listen -ErrorAction SilentlyContinue
if ($existingServer) {
  Add-Content -LiteralPath $OutLog -Value "$(Get-Date -Format s) Local production server already listening on 127.0.0.1:4321."
  exit 0
}

if (-not (Test-Path -LiteralPath (Join-Path $ProjectRoot "dist\index.html"))) {
  Add-Content -LiteralPath $ErrLog -Value "$(Get-Date -Format s) Missing dist/index.html. Run npm.cmd ci and npm.cmd run build first."
  exit 1
}

Set-Location -LiteralPath $ProjectRoot
Start-Process -FilePath $Node `
  -ArgumentList @("`"$LocalServer`"") `
  -WorkingDirectory $ProjectRoot `
  -WindowStyle Hidden `
  -RedirectStandardOutput $OutLog `
  -RedirectStandardError $ErrLog

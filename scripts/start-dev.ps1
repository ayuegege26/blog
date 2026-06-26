$ProjectRoot = Split-Path -Parent $PSScriptRoot
$OutLog = Join-Path $ProjectRoot ".astro-dev.log"
$ErrLog = Join-Path $ProjectRoot ".astro-dev.err.log"

$existingServer = Get-NetTCPConnection -LocalAddress "127.0.0.1" -LocalPort 4321 -State Listen -ErrorAction SilentlyContinue
if ($existingServer) {
  Add-Content -LiteralPath $OutLog -Value "$(Get-Date -Format s) Astro dev server already listening on 127.0.0.1:4321."
  exit 0
}

Set-Location -LiteralPath $ProjectRoot
Start-Process -FilePath "C:\Program Files\nodejs\npm.cmd" `
  -ArgumentList @("run", "dev", "--", "--host", "127.0.0.1") `
  -WorkingDirectory $ProjectRoot `
  -WindowStyle Hidden `
  -RedirectStandardOutput $OutLog `
  -RedirectStandardError $ErrLog

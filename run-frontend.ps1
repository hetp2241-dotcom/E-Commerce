$env:NEXT_PUBLIC_API_URL = 'http://localhost:8002/api'

Set-Location (Join-Path $PSScriptRoot 'frontend')

& 'C:\Program Files\nodejs\npm.cmd' run dev *>> (Join-Path $PSScriptRoot 'logs\frontend-live.log')

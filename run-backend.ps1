Set-Location $PSScriptRoot

& 'C:\Users\pkunj\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'backend\manage.py' `
  'runserver' `
  '127.0.0.1:8002' `
  '--noreload' *>> 'logs\backend-8002-live.log'

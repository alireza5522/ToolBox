@echo off &setlocal
if "%~1"=="" (set "root=.") else set "root=%~1"
set "pre0=                                    "
pushd %root%
call:dirtree "%CD%" "1" "1"
popd
goto:eof

:dirtree
setlocal
call set "pre=%%pre0:~-%~2%%
set /a ccount=%~3
set /a tcount=%~2+2
set /a dcount=0
for /d %%i in (*) do set /a dcount+=1
echo( %pre%{
echo(  %pre%"type": "folder",
echo(  %pre%"name": "%~nx1",
set "fpath=%~f1"
set "fpath=%fpath:\\=/%"
echo(  %pre%"path": "%fpath:\=\\%",
echo(  %pre%"childno": %ccount%,
if %dcount% equ 0 echo(  %pre%"subchilds": %dcount%
if %dcount% gtr 0 (
    echo(  %pre%"subchilds": %dcount%,
    echo(  %pre%"children": [
    for /d %%i in (*) do (
        for /f %%j in ('call echo "%%dcount%%"') do (
            cd "%%i"
            call:dirtree "%%i" "%tcount%" "%%j"
            cd ..
        )
        set /a dcount-=1
    )
    echo(  %pre%]
)
if %ccount% equ 1 (echo  %pre%}) else echo( %pre%},
endlocal
goto:eof

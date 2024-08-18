setlocal

set "folders=easy_datetime data_utils easy_utils"

set /p input=input commit message:
set /p branch=input branch:

for %%i in (%folders%) do (
    @echo off
    echo going to %%i
    cd %%i
    git add . && git commit -m "%DATE% %TIME%, %input%" && git push origin %branch% -f
    cd ..
)

endlocal

pause
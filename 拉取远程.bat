setlocal

set "folders=easy_datetime data_utils easy_utils"
set /p branch=input branch:

for %%i in (%folders%) do (
    echo Pulling changes in %%i
    cd %%i
    git fetch --all && git reset --hard origin/%branch%
    cd ..
)

endlocal

pause
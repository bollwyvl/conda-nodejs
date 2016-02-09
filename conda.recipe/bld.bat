mkdir %PREFIX%\Scripts
copy bin\npm.cmd %PREFIX%\Scripts
python %RECIPE_DIR%\win_download.py
npm install -g npm
if errorlevel 1 exit 1

mkdir %PREFIX%\Scripts
copy bin\npm.cmd %PREFIX%\Scripts
mkdir %PREFIX%\Scripts\node_modules
mkdir %PREFIX%\Scripts\node_modules\npm
xcopy /E * %PREFIX%\Scripts\node_modules\npm
python %RECIPE_DIR%\win_download.py
copy %PREFIX%\Scripts\iojs.exe %PREFIX%\Scripts\node.exe
copy %PREFIX%\Scripts\iojs.lib %PREFIX%\Scripts\node.lib
if errorlevel 1 exit 1

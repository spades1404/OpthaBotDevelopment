cd Assets
type reallyimportanttext.txt
cd ..
python -m pip install --upgrade pip setuptools wheel virtualenv
python -m virtualenv kivy_venv

CALL kivy_venv\Scripts\activate.bat

pip install kivy_deps.glew kivy_deps.sdl2 kivy_deps.gstreamer kivy kivy_examples --pre
pip install -r requirements.txt

python main.pyw


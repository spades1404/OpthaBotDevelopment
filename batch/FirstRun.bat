cd ..
python -m pip install --upgrade pip setuptools wheel virtualenv
python -m virtualenv kivy_venv
pip install kivy_deps.glew kivy_deps.sdl2 kivy_deps.gstreamer kivy kivy_examples --pre
pip install -r requirements.txt
pip install kivymd
python main.py
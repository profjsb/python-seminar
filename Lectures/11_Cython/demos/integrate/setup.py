from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

setup(
    ext_modules=cythonize(
       [Extension("integrate_compiled", ["integrate_compiled.pyx"])], 
        compiler_directives={'language_level': 3}
    )
)
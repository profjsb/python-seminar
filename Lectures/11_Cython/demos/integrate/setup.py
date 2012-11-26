from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  cmdclass = {'build_ext': build_ext},
  ext_modules = [
    Extension("integrate_compiled", ["integrate.py"]),
    Extension("integrate_types", ["integrate_types.pyx"]),
    Extension("integrate_cy", ["integrate_cy.pyx"]),
    Extension("integrate_any", ["integrate_any.pyx"])
  ]
)


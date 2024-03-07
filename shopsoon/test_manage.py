import unittest
from manage import main

class TestMain(unittest.TestCase):
    
    def test_main(self):
        # Test that main() runs without errors
        main()

    def test_main_import_error(self):
        # Mock import error and check it raises ImportError
        import builtins
        real_import = builtins.__import__
        def mock_import_error(name, globals, locals, fromlist, level):
            if name == 'django.core.management':
                raise ImportError()
            return real_import(name, globals, locals, fromlist, level)
        builtins.__import__ = mock_import_error
        
        with self.assertRaises(ImportError):
            main()
        
        builtins.__import__ = real_import


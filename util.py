def get_file_extension(track,lang):
    ext = {
        'java': '.java',
        'java7': '.java',
        'java8': '.java',
        'python': '.py',
        'python3': '.py',
        'python2': '.py',
        'csharp': '.cs',
        'javascript': '.js',
        'c': '.c',
        'cpp14':'.cpp',
        'cpp':'.cpp',
        'sql': '.sql',
        'mysql': '.sql',
        'oracle': '.sql'
    }
    return ext[lang] or ext[track]


from SublimeLinter.lint import NodeLinter


class Jscs(NodeLinter):
    npm_name = 'jscs'
    cmd = 'jscs -r checkstyle'
    regex = (
        r'^\s+?<error line="(?P<line>\d+)" '
        r'column="(?P<col>\d+)" '
        # jscs always reports with error severity; show as warning
        r'severity="(?P<warning>error)" '
        r'message="(?P<message>.+?)"'
    )
    multiline = True
    tempfile_suffix = 'js'
    defaults = {
        'selector': 'source.js - meta.attribute-with-value'
    }

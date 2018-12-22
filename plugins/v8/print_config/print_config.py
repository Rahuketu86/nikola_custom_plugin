from nikola.plugin_categories import Command

# You have to inherit Command for this to be a
# command plugin:

class CommandServe(Command):
    """Start test server."""

    name = "print_config"
    # doc_usage = "[options]"
    doc_purpose = "Print Site Configuration"

    # cmd_options = (
    #     {
    #         'name': 'port',
    #         'short': 'p',
    #         'long': 'port',
    #         'default': 8000,
    #         'type': int,
    #         'help': 'Port number (default: 8000)',
    #     },
    #     {
    #         'name': 'address',
    #         'short': 'a',
    #         'long': '--address',
    #         'type': str,
    #         'default': '127.0.0.1',
    #         'help': 'Address to bind (default: 127.0.0.1)',
    #     },
    # )

    def _execute(self, options, args):
        """Print Site Configuration"""
        print(self.site.config)
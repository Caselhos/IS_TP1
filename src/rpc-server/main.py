import signal
import sys
from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer


from functions.sendxmltodb import xmltodb
from functions.validate_xml_with_schema import validate_xml_with_schema
from functions.softdelete import softdelete
from functions.query1 import listarTitulo
from functions.query2 import listarAlbunsPorAno



class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('0.0.0.0', 9000), allow_none=True, requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def signal_handler(signum, frame):
        print("received signal")
        server.server_close()

        # perform clean up, etc. here...
        print("exiting, gracefully")
        sys.exit(0)


    # signals
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # register both functions
    server.register_function(xmltodb)
    server.register_function(validate_xml_with_schema)
    server.register_function(softdelete)
    server.register_function(listarTitulo)
    server.register_function(listarAlbunsPorAno)

    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()

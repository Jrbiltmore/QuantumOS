import asyncio
from aiocoap import *

class CoAPServer:
    def __init__(self, port=5683):
        self.port = port

    async def handle_request(self, request):
        """Handles incoming CoAP requests and returns a response."""
        if request.code == GET and request.opt.uri_path == ('hello',):
            payload = b"Hello from CoAP server!"
            return Message(code=CONTENT, payload=payload)
        else:
            return Message(code=NOT_FOUND, payload=b"Resource not found")

    async def start_server(self):
        """Starts the CoAP server."""
        # Create a CoAP protocol instance
        protocol = await Context.create_server_context()

        # Add a resource to the server
        protocol.add_resource(('hello',), self.handle_request)

        print(f"CoAP server running on port {self.port}")
        await asyncio.get_event_loop().create_future()  # Run forever

if __name__ == "__main__":
    server = CoAPServer()
    asyncio.run(server.start_server())

#!/usr/bin/python3
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Serve UTF-8 XML through HTTP and TLS on independent loopback ports."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import ssl
import sys
from threading import Thread

class XmlHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = b'<?xml version="1.0" encoding="UTF-8"?><test/>\n'
        self.send_response(200)
        self.send_header("Content-Type", "application/xml; charset=UTF-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

directory = Path(sys.argv[1])
with HTTPServer(("127.0.0.1", 0), XmlHandler) as http, HTTPServer(("127.0.0.1", 0), XmlHandler) as https:
    tls = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    tls.load_cert_chain(directory / "cert.pem", directory / "key.pem")
    https.socket = tls.wrap_socket(https.socket, server_side=True)
    Thread(target=http.serve_forever, daemon=True).start()
    (directory / "ports.tmp").write_text(f"{http.server_port} {https.server_port}\n")
    (directory / "ports.tmp").replace(directory / "ports")
    https.serve_forever()

import java . io .*;

import java . net .*;

public class MReceiver {

	public static void main ( String [] args ) {

		byte [] inBuf = new byte [256];

		try {

			MulticastSocket socket = new MulticastSocket (8888) ;

			InetAddress address = InetAddress . getByName (" 224.2.2.3 ");

			socket.joinGroup ( address );

			while ( true ) {

				DatagramPacket inPacket = new DatagramPacket ( inBuf , inBuf . length );

				socket.receive ( inPacket );

				String msg = new String ( inBuf , 0 , inPacket . getLength () ) ;

				System.out.println (" From " + inPacket . getAddress () + " Msg : " + msg ) ;

			}
		} catch ( IOException ioe ) {

			System.out.println ( ioe );

		}

	}

}
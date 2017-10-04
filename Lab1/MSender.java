import java . io .*;

import java . net .*;

public class MSender {

	public static void main ( String [] args ) {

		byte [] outBuf ;

		final int PORT = 8888;

		try {

			DatagramSocket socket = new DatagramSocket () ;

			long counter = 0;

			while ( true ) {

				counter ++;

				outBuf = (" Tomas Rezende " + counter ).getBytes () ;

				InetAddress address = InetAddress.getByName (" 224.2.2.3 ");

				DatagramPacket outPacket = new DatagramPacket ( outBuf , outBuf.length , address , PORT );

				socket.send ( outPacket ) ;

				System.out.println (" Server sends : Ola");

				try { Thread.sleep (500) ; }

				catch ( InterruptedException ie ) {}

	 		}

		} catch ( IOException ioe ) { System . out . println ( ioe ); }

	}

}
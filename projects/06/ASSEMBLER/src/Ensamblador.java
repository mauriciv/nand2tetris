import java.io.IOException;

public class Ensamblador {

	public static void main(String[] args) throws IOException {

		if (args.length != 0){
			Parser parser = new Parser(args[0]);
			while (parser.hasMoreCommands()){
				System.out.println(parser.lineaActual);
				parser.advance();
			}
		}
		else{
			System.out.println("Error. No se especifico ningun archivo.");
		}

	}
}

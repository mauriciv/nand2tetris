
public class Ensamblador {

	public static void main(String[] args) {

		if (args.length != 0){
			Parser parser = new Parser(args[0]);
			System.out.println(parser.lineaActual);
		}
		else{
			System.out.println("Error. No se especifico ningun archivo.");
		}

	}
}

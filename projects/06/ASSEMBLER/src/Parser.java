import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Parser {
	
	public static final int A_COMMAND = 0;
	public static final int C_COMMAND = 1;
	public static final int L_COMMAND = 2;
	private static final int CANTLIMITECARACTERES = 1000000;
	public String lineaActual;
	public int nroDeLineaActual = 0;

	private BufferedReader archivoAsm;
	

	Parser(String archivo){

		try{
			FileReader fileReader = new FileReader(archivo);
			archivoAsm = new BufferedReader(fileReader); 
			lineaActual = archivoAsm.readLine();
            lineaActual = lineaActual.trim();
			archivoAsm.mark(CANTLIMITECARACTERES);
		}
		catch (FileNotFoundException e){
			System.out.println("Error. No se encontro el archivo " + archivo);
		} catch (IOException e) {
			System.out.println("Error. No se pudo leer el archivo" + archivo);
		}
		
	}

	public boolean hasMoreCommands() throws IOException{
		archivoAsm.mark(CANTLIMITECARACTERES);
		String lineaSiguiente = archivoAsm.readLine();

		if (lineaSiguiente == null){
			archivoAsm.reset();
			return false;
		}
		return true;
	}

	/**
	 * Avanza hasta el siguiente comando de assembly, ignorando las lineas
	 * vacias y lineas de comentarios
	 * @throws IOException
	 */
	public void advance() throws IOException{
		lineaActual = archivoAsm.readLine();
		if (lineaActual == null){
			return;
		}
		lineaActual= lineaActual.trim();
		if ( lineaActual.isEmpty() || lineaActual.startsWith("//") ){
			this.advance();
		} else {
			nroDeLineaActual++;
		}

	}
	
	public int commandType(){
		return 0;
		
	}
	
	public String symbol(){
		return lineaActual;
		
	}

	public String dest(){
		return lineaActual;
		
	}

	public String comp(){
		return lineaActual;
		
	}

	public String jump(){
		return lineaActual;
		
	}
	
}
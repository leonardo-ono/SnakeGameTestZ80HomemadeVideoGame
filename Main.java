import java.io.BufferedReader;
import java.io.FileReader;

// font_8x8_reversed
public class Main {
    
    public static byte reverseBits(byte n) {
        byte reversed = 0;
        for (int i = 0; i < 8; i++) {
            reversed <<= 1; // Desloca um bit para a esquerda
            reversed |= (n & 1); // Adiciona o bit menos significativo de n ao resultado
            n >>= 1; // Desloca um bit para a direita para verificar o próximo bit
        }
        return reversed;
    }

    public static void main(String[] args) throws Exception {
        System.out.println("teste");

        BufferedReader br = new BufferedReader(new FileReader("font_8x8.txt"));
        String line;

        while ((line = br.readLine()) != null) {
            //System.out.println(line);
            System.out.print("db ");
            String[] datas = line.split("\s");
            for (int i = 1; i < 9; i++) {
                String data = datas[i].replace(",", "");
                data = data.substring(2);
                int value = Integer.parseInt(data, 16);
                int reversedValue = reverseBits((byte) value) & 0xff;
                String reversedHex = "00" + Integer.toHexString(reversedValue);
                reversedHex = reversedHex.substring(reversedHex.length() - 2, reversedHex.length());
                //System.out.print("[" + data + "=" + value + "=" + reversedValue + "]");
                //System.out.print("[" + data + "=" + reversedHex + "]");
                System.out.print("0x" + reversedHex + (i < 8 ? ", " : " ; " + datas[10]));
            }
            System.out.println();
        }

        br.close();
    }    
}

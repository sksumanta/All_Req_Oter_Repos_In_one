public class HollowTriangle {
  public static void main(String[] args) {
 
      int height = 10;  
 
      for ( int i=1 ; i<=height ; i++ ) {
         for ( int j=1 ; j <= i ; j++ ) {
            if(i==1 || i==2 || i==height || j==1 | j==i)
              System.out.print("*");
            else 
              System.out.print(" ");
         }
         System.out.println();
      }
   }
}

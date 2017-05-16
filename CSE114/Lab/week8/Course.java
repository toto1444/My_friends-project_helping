public class Course {

   String name;
   int numOfCredits;
   boolean isMandatory;
   String letterGrade;

   Course(String name){
      this.name = name;
   }

   public String getName() {
      return name;
   }
   public void setName(String name) {
      this.name = name;
   }
   public int getNumOfCredits() {
      return numOfCredits;
   }
   public void setNumOfCredits(int numOfCredits) {
      this.numOfCredits = numOfCredits;
   }
   public boolean isMandatory() {
      return isMandatory;
   }
   public void setMandatory(boolean isMandatory) {
      this.isMandatory = isMandatory;
   }
   public String getLetterGrade() {
      return letterGrade;
   }
   public void setLetterGrade(String letterGrade) {
      this.letterGrade = letterGrade;
   }

   String getStringValue(){
      String s = "";
      s += name + " takes " + numOfCredits + " credits.";
      return s;
   }
}

public class outer{
    int n;
    int m;
    public class Leedonggun() {
        int n;
        public class InnerPublic{
            int n;
    
            public void f(){
                n = 1;
                m = 2;
                this.n = 3;
                super.n = 7;
            }
        }
    }

    public void main(String[] args){
        InnerPublic ip = new InnerPublic();
        System.out.println(InnerPublic.n);
        System.out.println(InnerPublic.f().n);
        System.out.println(outer.n);

    }
}
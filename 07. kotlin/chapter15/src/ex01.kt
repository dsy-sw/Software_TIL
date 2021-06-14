

data class Human(var name: String, var age: Int, var addr: String = "서울"){
//    override fun equals(other: Any?): Boolean {
//        if (other is Human) {       // other가 human 인스턴스인가?
//            val h = other as Human      // Any에서 Human으로 타입 캐스팅
//            return name == other.name && age == other.age && addr == other.addr
//        } else {        // other가 human이 아닌 경우 false로 판정
//            return false
//        }
//        // python : __eq__()
//    }
//    override fun hashCode(): Int {
//        return super.hashCode()
//    }
//
//    override fun toString() = "$name $age $addr"        // python : __str__()
}


fun main() {
    val h1 = Human("홍길동", 20)
    val h2 = Human("고길동", 40, "수원")
    val h3 = Human("고길동", 40, "수원")

    println(h1)
    println(h2)
    println(h3)

    //내용이 같은가 검사, 참조가 같은가 : ===
    println(h1==h2)
    println(h2==h3)


}
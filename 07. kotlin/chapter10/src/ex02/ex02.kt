import com.sun.jdi.connect.Connector

val patronList2 = mutableListOf<String>("Eli", "Mordoc", "Shphie")

fun main(args: Array<String>) {
    patronList2.remove("Eli")
    patronList2.add("Alex")
    println(patronList2)
    patronList2.add(0, "Alex")

    patronList2[0] = "Alexis"
    println(patronList2)
    patronList.forEach { println("좋은 밤입니다. $it 님") }
}
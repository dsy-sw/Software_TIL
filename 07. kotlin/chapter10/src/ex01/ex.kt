import java.util.stream.Collectors.toList

const val TAVERN_NAME = "Taernyl's Folly"

var playerGold = 10
var playerSilver = 10
val patronList = listOf<String>("Eli", "Mordoc", "Sophie")
val fifthPatron = patronList.getOrNull (4) ?: "Unknown Patron"
fun main(args: Array<String>){
    println(patronList[0])
    println(patronList)
    println()

    patronList.apply{
        println(first())
        println(last())
    }

}

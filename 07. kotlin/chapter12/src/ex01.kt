import game.Dice
import game.Player

fun main(args: Array<String>){
    val player = Player()
    player.name = "estragon"
    println(player.name + "TheBrave")
    player.castFireball()

    val myD6 = Dice()
    println(myD6.rolledValue)
    println(myD6.rolledValue)
    println(myD6.rolledValue)

    myD6.apply {
        println(rolledValue)
        println(rolledValue)
        println(rolledValue)
    }
}
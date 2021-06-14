fun main(args: Array<String>){
    val player = Player("Madrigal", 89, true, false)
    println(player)
    println(player.name)
    println(player.healthPoints)
    println(player.isBlessed)

    val player2 = Player("Hong gildong")
   println(player2)
    player2.apply {println("$name $healthPoints $isBlessed")}

    println(player2.hometown)
}
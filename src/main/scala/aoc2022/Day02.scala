package aoc2022

/*
0. A X ROCK = OUTCOME + 1
1. B Y PAPER = OUTCOME + 2
2. C Z SCISSORS = OUTCOME + 3

LOSE
B X -> 0+1
C Y -> 0+2
A Z -> 0+3
DRAW
A X -> 3+1
B Y -> 3+2
C Z -> 3+3
WIN
C X -> 6+1
A Y -> 6+2
B Z -> 6+3

*/
object Day02:

  private def getPointsPart1(pair: Array[Int]): Int =
    (3 + pair.last - pair.head) % 3 match {
    case 0 => 3 + (pair.last + 1)
    case 1 => 6 + (pair.last + 1)
    case 2 => 0 + (pair.last + 1)
  }

  def part1(input: Seq[Array[String]]): Int =
    input.map(pair => Array(pair.head.toCharArray.head.toInt - 'A', pair.last.toCharArray.head.toInt - 'X')).map(getPointsPart1).sum

  def part2(input: Seq[Array[String]]): Int =
      val order = Seq("", "B X", "C X", "A X", "A Y", "B Y", "C Y", "C Z", "A Z", "B Z").zipWithIndex.toMap // Not my solution
      input.map(value => order.getOrElse(value.mkString(" "), 0)).sum

  def main(args: Array[String]): Unit =
    val data = io.Source.fromResource("aoc2022/Day02.in").getLines().map(_.split(" ").take(2)).toSeq
    println(part1(data))
    println(part2(data))
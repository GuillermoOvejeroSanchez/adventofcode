package aoc2022

import org.scalatest.funsuite.AnyFunSuite

class Day02Test extends  AnyFunSuite{
  val sample: Seq[Array[String]] = io.Source.fromResource("aoc2022/Day02test.in").getLines().map(_.split(" ").take(2)).toSeq

  test("A should convert to 65") {
    assert("A".toCharArray.head.toInt == 65)
  }
  test("Part 1 should handle sample input correctly") {
    assert(Day02.part1(sample) == 45)
  }

  test("String 1 should convert to int 1") {
    assert("1".toInt == 1)
  }

}

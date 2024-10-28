package com.falon.habitbackend

import cats.effect.{IO, IOApp}

object Main extends IOApp.Simple:
  val run = HabitbackendServer.run[IO]

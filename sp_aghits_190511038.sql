-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Waktu pembuatan: 10 Sep 2022 pada 10.19
-- Versi server: 8.0.30
-- Versi PHP: 8.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sp_aghits_190511038`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `books`
--

CREATE TABLE `books` (
  `id` int NOT NULL,
  `writer_id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `synopsis` text NOT NULL,
  `picture` varchar(255) NOT NULL,
  `pages` int NOT NULL,
  `rent_cost` bigint NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `books`
--

INSERT INTO `books` (`id`, `writer_id`, `name`, `synopsis`, `picture`, `pages`, `rent_cost`, `created_at`, `updated_at`) VALUES
(1, 1, 'Harry Potter and the Sorcerer\'s Stone', 'Harry Potter, an eleven-year-old orphan, discovers that he is a wizard and is invited to study at Hogwarts. Even as he escapes a dreary life and enters a world of magic, he finds trouble awaiting him.', 'books/harpot1.jpeg', 309, 25000, '2022-09-10 05:14:05', '2022-09-10 08:25:04'),
(2, 1, 'Harry Potter and the Chamber of Secrets', 'A house-elf warns Harry against returning to Hogwarts, but he decides to ignore it. When students and creatures at the school begin to get petrified, Harry finds himself surrounded in mystery.', 'books/harpot2.jpeg', 251, 30000, '2022-09-10 05:16:06', '2022-09-10 08:25:06'),
(3, 1, 'Harry Potter and the Prisoner of Azkaban', 'Harry, Ron and Hermoine return to Hogwarts just as they learn about Sirius Black and his plans to kill Harry. However, when Harry runs into him, he learns that the truth is far from reality.', 'books/harpot3.jpeg', 317, 30000, '2022-09-10 05:16:06', '2022-09-10 08:25:08'),
(4, 1, 'Harry Potter and the Goblet of Fire', 'When Harry gets chosen as the fourth participant in the inter-school Triwizard Tournament, he is unwittingly pulled into a dark conspiracy that slowly unveils its dangerous agenda.', 'books/harpot4.jpeg', 636, 40000, '2022-09-10 05:18:06', '2022-09-10 08:25:10'),
(5, 1, 'Harry Potter and the Order of the Phoenix', 'Harry Potter and Dumbledore\'s warning about the return of Lord Voldemort is not heeded by the wizard authorities who, in turn, look to undermine Dumbledore\'s authority at Hogwarts and discredit Harry.', 'books/harpot5.jpeg', 870, 55000, '2022-09-10 05:18:06', '2022-09-10 08:25:12'),
(6, 1, 'Harry Potter and the Half-Blood Prince', 'Dumbledore and Harry Potter learn more about Voldemort\'s past and his rise to power. Meanwhile, Harry stumbles upon an old potions textbook belonging to a person calling himself the Half-Blood Prince.', 'books/harpot6.jpeg', 652, 35000, '2022-09-10 05:20:15', '2022-09-10 08:25:14'),
(7, 1, 'Harry Potter and the Deathly Hallows', 'After Voldemort takes over the Ministry of Magic, Harry, Ron and Hermione are forced into hiding. They try to decipher the clues left to them by Dumbledore to find and destroy Voldemort\'s Horcruxes.', 'books/harpot7.jpeg', 769, 55000, '2022-09-10 05:20:15', '2022-09-10 08:25:16'),
(8, 3, 'The Hobbit', 'Bilbo Baggins (Martin Freeman) lives a simple life with his fellow hobbits in the shire, until the wizard Gandalf (Ian McKellen) arrives and convinces him to join a group of dwarves on a quest to reclaim the kingdom of Erebor. The journey takes Bilbo on a path through treacherous lands swarming with orcs, goblins and other dangers, not the least of which is an encounter with Gollum (Andy Serkis) and a simple gold ring that is tied to the fate of Middle Earth in ways Bilbo cannot even fathom.', 'books/hobbit.jpg', 310, 25000, '2022-09-10 05:23:14', '2022-09-10 08:27:47'),
(9, 3, 'Tbe Lord of the Rings', 'The future of civilization rests in the fate of the One Ring, which has been lost for centuries. Powerful forces are unrelenting in their search for it. But fate has placed it in the hands of a young Hobbit named Frodo Baggins (Elijah Wood), who inherits the Ring and steps into legend. A daunting task lies ahead for Frodo when he becomes the Ringbearer - to destroy the One Ring in the fires of Mount Doom where it was forged.', 'books/lotr.jpeg', 1178, 60000, '2022-09-10 05:23:14', '2022-09-10 08:27:55'),
(10, 2, 'A Game of Thrones', 'Years after a rebellion spurred by a stolen bride to be and the blind ambitions of a mad King, Robert of the house Baratheon (Mark Addy) sits on the much desired Iron Throne. In the mythical land of Westeros, nine noble families fight for every inch of control and every drop of power.', 'books/agameofthrones.webp', 694, 45000, '2022-09-10 05:25:28', '2022-09-10 08:28:23'),
(11, 2, 'A Clash of Kings', 'A Clash of Kings picks up the story where A Game of Thrones leaves off. The Seven Kingdoms are plagued by civil war, the Night\'s Watch mounts a reconnaissance force north of the Wall, and in the distant east, Daenerys Targaryen continues her quest to return to the Seven Kingdoms and claim her birthright.', 'books/aclashofkings.jpg', 768, 50000, '2022-09-10 05:29:14', NULL),
(12, 2, 'A Storm of Swords', 'A Storm of Swords continues the story where A Clash of Kings ended. The novel describes the increasingly vicious War of Five Kings in Westeros, Daenerys\'s strengthening forces in the East, and the oncoming threat of the Others, a ghostly army that is nearly invincible.', 'books/astormofswords.jpg', 973, 60000, '2022-09-10 05:29:14', NULL),
(13, 2, 'A Feast for Crows', 'A Feast for Crows focuses on the Lannister family\'s continuing consolidation of power following victory in the “War of the Five Kings.” Specifically, it follows the events precipitated by the murder of Tywin Lannister, who had been de facto ruler of Westeros. In his place, his daughter Cersei, seizes power.', 'books/afeastforcrows.jpg', 753, 50000, '2022-09-10 05:29:14', NULL),
(14, 2, 'A Dance with Dragons', 'UPDATE: In the aftermath of a colossal battle, the future of the Seven Kingdoms hangs in the balance—beset by newly emerging threats from every direction. In the east, Daenerys Targaryen, the last scion of House Targaryen, rules with her three dragons as queen of a city built on dust and death.', 'books/adancewithdragons.jpg', 1056, 75000, '2022-09-10 05:29:14', '2022-09-10 10:11:13');

-- --------------------------------------------------------

--
-- Struktur dari tabel `rents`
--

CREATE TABLE `rents` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `book_id` int NOT NULL,
  `rent_duration` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `rents`
--

INSERT INTO `rents` (`id`, `user_id`, `book_id`, `rent_duration`, `created_at`, `updated_at`) VALUES
(1, 1, 10, 2, '2022-09-10 05:29:41', NULL),
(3, 2, 5, 4, '2022-09-10 10:05:39', NULL),
(4, 3, 14, 4, '2022-09-10 10:05:48', NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `created_at`, `updated_at`) VALUES
(1, 'admin', '21232f297a57a5a743894a0e4a801fc3', '2022-09-10 05:04:17', '2022-09-10 07:40:00'),
(2, 'aghits', 'a6da60a08bef263884bcef09658888fe', '2022-09-10 05:04:26', NULL),
(3, 'hatsu', 'eb84317649336141a3a99821e27df0b4', '2022-09-10 06:07:29', NULL),
(6, 'usera', '697aa03927398125bb6282e2f414a6be', '2022-09-10 10:15:11', NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `writers`
--

CREATE TABLE `writers` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `birth_date` date NOT NULL,
  `picture` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `writers`
--

INSERT INTO `writers` (`id`, `name`, `birth_date`, `picture`, `created_at`, `updated_at`) VALUES
(1, 'J.K. Rowling', '1965-07-31', 'writers/jkrowling.jpeg', '2022-09-10 05:05:42', '2022-09-10 10:07:32'),
(2, 'George R. R. Martin', '1948-09-20', 'writers/georgerrmartin.jpg', '2022-09-10 05:06:49', NULL),
(3, 'J. R. R. Tolkien', '1892-01-03', 'writers/jrrtolkien.jpeg', '2022-09-10 05:07:13', '2022-09-10 10:07:36');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`),
  ADD KEY `writers_writer_id` (`writer_id`),
  ADD KEY `name` (`name`);

--
-- Indeks untuk tabel `rents`
--
ALTER TABLE `rents`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rents_user_id` (`user_id`),
  ADD KEY `rents_book_id` (`book_id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`) USING BTREE;

--
-- Indeks untuk tabel `writers`
--
ALTER TABLE `writers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `books`
--
ALTER TABLE `books`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT untuk tabel `rents`
--
ALTER TABLE `rents`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `writers`
--
ALTER TABLE `writers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_writer_id` FOREIGN KEY (`writer_id`) REFERENCES `writers` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `rents`
--
ALTER TABLE `rents`
  ADD CONSTRAINT `fk_rents_book_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_rents_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

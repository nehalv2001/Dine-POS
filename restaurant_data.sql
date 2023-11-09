-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 24, 2023 at 06:17 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `restaurant_data`
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id` int(10) NOT NULL,
  `Bill_Number` int(10) NOT NULL,
  `dishes_cost` varchar(10) NOT NULL,
  `drinks_cost` varchar(10) NOT NULL,
  `service_charge` varchar(10) NOT NULL,
  `subtotal` varchar(10) NOT NULL,
  `total` varchar(10) NOT NULL,
  `Time` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id`, `Bill_Number`, `dishes_cost`, `drinks_cost`, `service_charge`, `subtotal`, `total`, `Time`) VALUES
(1, 9050, '650₹', '650₹', '50₹', '650₹', '700₹', '2023-04-24 21:37:57'),
(2, 5447, '270₹', '270₹', '50₹', '330₹', '380₹', '2023-04-24 21:39:43'),
(3, 3756, '360₹', '360₹', '50₹', '420₹', '470₹', '2023-04-24 21:40:26'),
(4, 8024, '480₹', '480₹', '50₹', '570₹', '620₹', '2023-04-24 21:45:39'),
(5, 8565, '820₹', '820₹', '50₹', '1010₹', '1060₹', '2023-04-24 21:46:12');

-- --------------------------------------------------------

--
-- Table structure for table `dishes`
--

CREATE TABLE `dishes` (
  `Gujarati Thali` varchar(10) NOT NULL,
  `Punjabi Thali` varchar(10) NOT NULL,
  `Chinese Noodles` varchar(10) NOT NULL,
  `Manchurian` varchar(10) NOT NULL,
  `Chinese Soup` varchar(10) NOT NULL,
  `Pavbhaji` varchar(10) NOT NULL,
  `Butter Bhaji` varchar(10) NOT NULL,
  `Pizza` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dishes`
--

INSERT INTO `dishes` (`Gujarati Thali`, `Punjabi Thali`, `Chinese Noodles`, `Manchurian`, `Chinese Soup`, `Pavbhaji`, `Butter Bhaji`, `Pizza`) VALUES
('80', '120', '110', '90', '70', '100', '130', '210');

-- --------------------------------------------------------

--
-- Table structure for table `dishes_2`
--

CREATE TABLE `dishes_2` (
  `Sandwich` varchar(10) NOT NULL,
  `Grill Sandwich` varchar(10) NOT NULL,
  `Biryani` varchar(10) NOT NULL,
  `Jira-Rice` varchar(10) NOT NULL,
  `Sada Dhosa` varchar(10) NOT NULL,
  `Masala Dhosa` varchar(10) NOT NULL,
  `Mysore Dhosa` varchar(10) NOT NULL,
  `Burger` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dishes_2`
--

INSERT INTO `dishes_2` (`Sandwich`, `Grill Sandwich`, `Biryani`, `Jira-Rice`, `Sada Dhosa`, `Masala Dhosa`, `Mysore Dhosa`, `Burger`) VALUES
('95', '110', '70', '80', '110', '100', '130', '60');

-- --------------------------------------------------------

--
-- Table structure for table `drinks`
--

CREATE TABLE `drinks` (
  `Chaas` varchar(10) NOT NULL,
  `Pepsi` varchar(10) NOT NULL,
  `Coke` varchar(10) NOT NULL,
  `Sprite` varchar(10) NOT NULL,
  `Sosyo` varchar(10) NOT NULL,
  `Juice` varchar(10) NOT NULL,
  `Mazza` varchar(10) NOT NULL,
  `Shake` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `drinks`
--

INSERT INTO `drinks` (`Chaas`, `Pepsi`, `Coke`, `Sprite`, `Sosyo`, `Juice`, `Mazza`, `Shake`) VALUES
('20', '30', '30', '30', '30', '40', '30', '60');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data`
--
ALTER TABLE `data`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

# EchoesOfEldoria

Welcome to EchoesOfEldoria, a turn-based strategy game built on the Solana blockchain! In this game, players engage in strategic battles using their unique characters to claim victory. The game leverages Solana's fast and secure blockchain to ensure a seamless and fair gaming experience.

## Table of Contents

- [Getting Started](#getting-started)
- [Game Overview](#game-overview)
- [Smart Contracts](#smart-contracts)
- [Building and Running](#building-and-running)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Rust and Cargo: [Install Rust](https://www.rust-lang.org/tools/install)
- Solana CLI: [Install Solana CLI](https://docs.solana.com/cli/install-solana-cli-tools)
- Node.js and npm: [Install Node.js](https://nodejs.org/)

### Installation

Clone the repository:

```sh
git clone https://github.com/yourusername/echoes-of-eldoria.git
cd echoes-of-eldoria
```

Install the dependencies:

```sh
cargo build-bpf
```

## Game Overview

EchoesOfEldoria is a turn-based strategy game where players control a team of characters, each with unique abilities. The objective is to strategically outmaneuver your opponent and deplete their characters' health to win the game.

### Characters

Each character has the following attributes:

- `mint`: Unique identifier for the character.
- `health`: Health points of the character.
- `hit`: Attack power of the character.
- `xp`: Experience points of the character.

### Game State

The game state is managed by the `GameState` struct, which includes:

- `is_initialized`: Indicates if the game is initialized.
- `initializer`: Public key of the player who initialized the game.
- `guest`: Public key of the guest player.
- Character attributes for both initializer and guest.
- `last_play_time`: Timestamp of the last move.
- `whose_turn`: Indicates whose turn it is to play.

### Actions

Players can perform actions such as:

- `Attack`: Engage in combat with the opponent's characters.
- `Move`: Move characters strategically on the board (implementation details pending).

## Smart Contracts

The core game logic is implemented in Rust using Borsh for serialization. The key structs are:

- `RandomNumber`: Represents a random number for game mechanics.
- `GameState`: Manages the state of the game.
- `Character`: Defines the attributes of a character.
- `Attack`: Represents an attack action.
- `PlayerAccount`: Tracks player stats.

## Building and Running

Compile the smart contracts:

```sh
cargo build-bpf
```

Deploy the contracts to the Solana blockchain:

```sh
solana program deploy path/to/your_program.so
```

Run the frontend (if applicable):

```sh
npm install
npm start
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

EchoesOfEldoria is licensed under the MIT License. See `LICENSE` for more information.

---

Enjoy playing EchoesOfEldoria! For any issues or support, please open an issue on GitHub.

---

This README provides a comprehensive overview of EchoesOfEldoria, including how to set up the development environment, game mechanics, and instructions for contributing. Feel free to reach out for any questions or further assistance!
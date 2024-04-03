const {
    ChatInputCommandInteraction,
    SlashCommandBuilder,
    SlashCommandUserOption,
    SlashCommandRoleOption,
    ModalBuilder,
    ActionRowBuilder,
    TextInputBuilder,
    TextInputStyle,
  } = require("/Users/domin/Desktop/Code Projects/coder/AD/PromptExercises/JS/discord");
  const mongoose = require('mongoose');
  const ExtendedClient = require("../../../class/ExtendedClient");

  mongoose.connect('mongodb://localhost:27017')
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('Error connecting to MongoDB:', err));
  
  module.exports = {
    structure: new SlashCommandBuilder()
      .setName("winner")
      .setDescription("Selects a winner and loser and the user who will be the winner and will receive a role.")
      .addUserOption((option) =>
        option
          .setName("winner")
          .setDescription("The user who will be the winner.")
          .setRequired(true)
      )
      .addRoleOption((option) =>
        option
          .setName("winner_role")
          .setDescription("The role that the winner will receive.")
          .setRequired(true)
      ),
    run: async (client, interaction) => {
      // Check if the user has the required permissions to use the command
      if (!interaction.member.roles.cache.has("1165968942741848114")) {
        return interaction.reply({
          content: "You do not have the required permissions to use this command.",
          ephemeral: true,
        });
      }
  
      const WinningStreak = new mongoose.Schema({
        userId: String,
        winningStreak: Number
      });

      const WinningStreakModel = mongoose.model('WinningStreak', WinningStreak);
      // Get the winner and loser users
      const winnerUser = interaction.options.getUser("winner");
      const loserUser = interaction.options.getUser("winner");
  
      // Get the winner role
      const winnerRole = interaction.options.getRole("winner_role");
  
      // Check if the winner user is in the database
      const winnerWinningStreak = await WinningStreakModel.findOne({ userId: winnerUser.id });
  
      // If the winner user is not in the database, create a new record
      if (!winnerWinningStreak) {
        await WinningStreakModel.create({ userId: winnerUser.id, winningStreak: 1 });
      } else {
        // Increment the winner user's winning streak
        await WinningStreakModel.updateOne({ userId: winnerUser.id }, { winningStreak: winnerWinningStreak.winningStreak + 1 });
      }
  
      // Check if the loser user is in the database
      const loserWinningStreak = await WinningStreakModel.findOne({ userId: loserUser.id });
  
      // If the loser user is in the database, remove their winning streak
      if (loserWinningStreak) {
        await WinningStreakModel.deleteOne({ userId: loserUser.id });
      }
  
      // Add the winner role to the winner user
      await winnerUser.roles.add(winnerRole);
  
      // Send a message to the winner and loser users
      await winnerUser.send("Congratulations, you won!");
      await loserUser.send("Sorry, you lost.");
  
      // Send a confirmation message to the interaction author
      await interaction.reply("The winner has been selected and the loser's winning streak has been removed.");
    },
  };
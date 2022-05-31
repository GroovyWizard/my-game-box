import React from "react";
import { StyleSheet, Text, View } from "react-native";
import Login from "./login";
export default function HomeScreen() {
  return (
    <View style={styles.container}>
        <Login />

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});

import React, { useState, useEffect } from "react";
import { API_BASE_URL } from "@env";
import { ActivityIndicator, ScrollView, View, Text } from "react-native";
import { Button, Tile } from "react-native-elements";
import AsyncStorage from "@react-native-async-storage/async-storage";

function GameScreen({ route }) {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [data, setData] = useState({});
  const { id } = route.params;

  const storeFavorite = async (value) => {
    try {
      console.log("executed");
      await AsyncStorage.setItem("@favorite", "ronaldo");
    } catch (e) {
      // saving error
    }
  };

  useEffect(() => {


    setLoading(true);
    fetch(`${API_BASE_URL}:8000/games/${id}/`)
      .then((response) => response.json())
      .then((data) => {
        if (typeof data !== "object") {
          setError("No movie available");
          return setLoading(false);
        }

        setLoading(false);
        setData(data);

        if (error) setError(null);
      })
      .catch((e) => {
        setLoading(false);
        setError("Fetching movies failed");
      });
  }, []);

  if (loading)
    return (
      <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
        <ActivityIndicator size="large" color="tomato" />
      </View>
    );
  if (error) return <Text>ERROR: {error}</Text>;

  const { name, publisher, banner_img, description } = data;
  return (
    <ScrollView>
      <Tile
        imageSrc={{
          uri: banner_img,
        }}
        title={name}
        featured
        caption={publisher}
      />
      <View
        style={{
          flexDirection: "row",
          padding: 20,
        }}
      >
        <Button title="Favoritar jogo" onPress={storeFavorite} />

        <View style={{ flex: 1 }}>
          <Text>{description}</Text>
        </View>
      </View>
    </ScrollView>
  );
}

export default GameScreen;

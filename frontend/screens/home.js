import React, { useEffect } from "react";
import { API_BASE_URL } from "@env";
import {
  SafeAreaView,
  Text,
  View,
  StyleSheet,
  ActivityIndicator,
} from "react-native";
import GameSection from "../components/gameSection";
import { ScrollView } from "react-native-gesture-handler";
import CarouselCards from "../components/carousel";
import mockData from "../sample-data.json";
import axios from "axios";


function HomeScreen({ navigation }) {
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState(null);
  const [data, setData] = React.useState([]);
  const [featured, setfeatured] = React.useState([]);

  const handlePress = ({ title, id }) =>
    navigation.navigate("Game", {
      id,
      title,
    });

  useEffect(() => {
    setLoading(true);
    fetch(`${API_BASE_URL}:8000/api/game/list/?option=featured`)
    // fetch("http://10.0.2.2:8000/api/game/list/?option=featured")
      .then((response) => response.json())
      .then((featured = []) => {
        if (!featured.length) {
          setError('Erro, jogos não encontrados :( ');
          return setLoading(false);
        }

        setLoading(false);
        setfeatured(featured);

        if (error) {
          console.log(error);
          setError(null);
        }
      })
      .catch((e) => {
        console.log(e)
        setLoading(false);
        setError('Erro.')
      });


    fetch(`${API_BASE_URL}:8000/api/game/list/?option=featured`)
      .then((response) => response.json())
      .then((data = []) => {
        if (!data.length) {
          setError("No games available");
          return setLoading(false);
        }

        setLoading(false);
        setData(data);

        if (error) {
          console.log(error);
          setError(null);
        };
      })
      .catch((e) => {
        console.log(e)
        setLoading(false);
        setError("Fetching games failed");
      });
  }, []);

  if (loading)
    return (
      <View style={styles.container}>
        <ActivityIndicator size="large" color="tomato" />
      </View>
    );
  if (error) return <Text>ERROR: {error}</Text>;

  return (
    <ScrollView>
      <ScrollView style={styles.scrollView}>
        {/* <Carousel data={featured} onPress={handlePress}>
        </Carousel> */}
        <CarouselCards data={data} > </CarouselCards>
        <GameSection
          onPress={handlePress}
          data={data}
          title="Jogos recentes"
        ></GameSection>

        <GameSection
          onPress={handlePress}
          data={featured}
          title="Jogos mais bem avaliados"
        ></GameSection>
       
        
      </ScrollView>
    </ScrollView>
  );
}

export default HomeScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  text: {
    fontSize: 12,
    padding: 10,
    textAlign: "center",
  },
});
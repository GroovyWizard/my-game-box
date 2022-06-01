import React from 'react'
import { View } from "react-native"
import Carousel from 'react-native-reanimated-carousel';

const CarouselCards = ({data}) => {
  return (
    <View>
      <Carousel
        width={300}
        height={150}
        data={[1, 2, 3]}
      />
      
    </View>

  )
}



export default CarouselCards

import { Storage } from '@ionic/storage';

class CharacterRequester {
  static store = new Storage();

  static async getStorage() {
    await this.store.create();
    return this.store;
  }
}

export default CharacterRequester;
import {User} from "./user";

export class Producer extends User {
  companyName: string;
  description: string;
  inHoliday: boolean;

  constructor(rawData) {
    super(rawData);

    this.companyName = rawData.companyName;
    this.description = rawData.description;
    this.inHoliday = rawData.inHoliday;
  }
}


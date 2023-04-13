<p><a href="https://www.beecrowd.com.br/repository/UOJ_2605_en.html">beecrowd.com.br/repository/UOJ_2605_en.html</a></p><hr>
                                          <div>
                                            <span>URI Online <strong>SQL</strong> | 2605 </span>
                                            <h1>Executive Representatives</h1>
                                            <div>
                                              <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
                                            </div>
                                            <strong>Timelimit: 1</strong>
                                          </div>
                                          <div>
                                          <div>
                                            <p>The financial sector needs a report on the providers of the products we sell. The reports include all categories, but for some reason, providers of products whose category is the executive, are not in the report.</p>
                                            <p>Your job is to return the names of the products and providers whose category ID is 6.</p>
                                          </div>
                                          <div>
                                          <h2>Schema</h2>
                                          <div>
                                          <table>
                                          <caption>products</caption>
                                          <tbody><tr>
                                          <td><strong>Column</strong></td>
                                          <td><strong>Type</strong></td>
                                        </tr>
                                        <tr>
                                          <td>id (PK)</td>
                                          <td>numeric</td>
                                        </tr>
                                        <tr>
                                          <td>name</td>
                                          <td>varchar</td>
                                        </tr>
                                        <tr>
                                          <td>amount</td>
                                          <td>numeric</td>
                                        </tr>
                                        <tr>
                                          <td>price</td>
                                          <td>numeric</td>
                                        </tr>
                                        <tr>
                                          <td>id_providers (FK)</td>
                                          <td>numeric</td>
                                        </tr>
                                        <tr>
                                          <td>id_categories (FK)</td>
                                          <td>numeric</td>
                                        </tr>
                                      </tbody></table>
                                      <table>
                                      <caption>providers</caption>
                                      <tbody><tr>
                                      <td><strong>Column</strong></td>
                                      <td><strong>Type</strong></td>
                                    </tr>
                                    <tr>
                                      <td>id (PK)</td>
                                      <td>numeric</td>
                                    </tr>
                                    <tr>
                                      <td>name</td>
                                      <td>varchar</td>
                                    </tr>
                                    <tr>
                                      <td>street</td>
                                      <td>varchar</td>
                                    </tr>
                                    <tr>
                                      <td>city</td>
                                      <td>varchar</td>
                                    </tr>
                                    <tr>
                                      <td>state</td>
                                      <td>char</td>
                                    </tr>
                                  </tbody></table>
                                  <table>
                                  <caption>categories</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>varchar</td>
                                </tr>
                              </tbody></table>
                            </div>
                          </div>
                          <div>
                          <h2>Tables</h2>
                          <div>
                          <table>
                          <caption>products</caption>
                          <tbody><tr>
                          <td><strong>id</strong></td>
                          <td><strong>name</strong></td>
                          <td><strong>amount</strong></td>
                          <td><strong>price</strong></td>
                          <td><strong>id_providers</strong></td>
                          <td><strong>id_categories</strong></td>
                        </tr>
                        <tr>
                          <td>1</td>
                          <td>Two-door wardrobe</td>
                          <td>100</td>
                          <td>800</td>
                          <td>6</td>
                          <td>8</td>
                        </tr>
                        <tr>
                          <td>2</td>
                          <td>Dining table</td>
                          <td>1000</td>
                          <td>560</td>
                          <td>1</td>
                          <td>9</td>
                        </tr>
                        <tr>
                          <td>3</td>
                          <td>Towel holder</td>
                          <td>10000</td>
                          <td>25.50</td>
                          <td>5</td>
                          <td>1</td>
                        </tr>
                        <tr>
                          <td>4</td>
                          <td>Computer desk</td>
                          <td>350</td>
                          <td>320.50</td>
                          <td>4</td>
                          <td>6</td>
                        </tr>
                        <tr>
                          <td>5</td>
                          <td>Chair</td>
                          <td>3000</td>
                          <td>210.64</td>
                          <td>3</td>
                          <td>6</td>
                        </tr>
                        <tr>
                          <td>6</td>
                          <td>Single bed</td>
                          <td>750</td>
                          <td>460</td>
                          <td>1</td>
                          <td>2</td>
                        </tr>
                      </tbody></table>
                      <table>
                      <caption>providers</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                      <td><strong>street</strong></td>
                      <td><strong>city</strong></td>
                      <td><strong>state</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Henrique</td>
                      <td>Av Brasil</td>
                      <td>Rio de Janeiro</td>
                      <td>RJ</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Marcelo Augusto</td>
                      <td>Rua Imigrantes</td>
                      <td>Belo Horizonte</td>
                      <td>MG</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Caroline Silva</td>
                      <td>Av São Paulo</td>
                      <td>Salvador</td>
                      <td>BA</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Guilerme Staff</td>
                      <td>Rua Central</td>
                      <td>Porto Alegre</td>
                      <td>RS</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Isabela Moraes</td>
                      <td>Av Juiz Grande</td>
                      <td>Curitiba</td>
                      <td>PR</td>
                    </tr>
                    <tr>
                      <td>6</td>
                      <td>Francisco Accerr</td>
                      <td>Av Paulista</td>
                      <td>São Paulo</td>
                      <td>SP</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>categories</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>old stock</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>new stock</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>modern</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>commercial</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>recyclable</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>executive</td>
                </tr>
                <tr>
                  <td>7</td>
                  <td>superior</td>
                </tr>
                <tr>
                  <td>8</td>
                  <td>wood</td>
                </tr>
                <tr>
                  <td>9</td>
                  <td>super luxury</td>
                </tr>
                <tr>
                  <td>10</td>
                  <td>vintage</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>name</strong></td>
          <td><strong>name</strong></td>
        </tr>
        <tr>
          <td>Computer desk</td>
          <td>Guilerme Staff</td>
        </tr>
        <tr>
          <td>Chair</td>
          <td>Caroline Silva</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>